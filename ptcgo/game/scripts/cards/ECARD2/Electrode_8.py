from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.attributes import AttrID


def _is_lightning_energy(card):
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)


def _super_dynamo_available(board, player_id, pokemon):
    if not is_in_active_spot(pokemon) or pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    discard = board.find_player_area(player_id, "discard")
    return any(_is_lightning_energy(card) for card in (discard.children if discard else []))


async def _super_dynamo(ctx):
    results = await ctx.flip_coins(1, "Super Dynamo")
    if not (results and results[0]):
        return
    await attach_from_discard(_is_lightning_energy, count=1, target="choice",
                              prompt="Choose a Lightning Energy card from your discard pile")(ctx)


card = PokemonCardDef(
    guid="119f5397-70a9-5710-aa8e-327a1ff07126",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Super Dynamo",
            game_text="Once during your turn (before your attack), if Electrode is your Active Pok\u00e9mon, you may flip a coin. If heads, choose a Lightning Energy card from your discard pile and attach it to 1 of your Pok\u00e9mon. This power can't be used if Electrode is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_super_dynamo_available,
            effect=unimplemented,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True, ignore_target_effects=True),
        ),
    ],
)