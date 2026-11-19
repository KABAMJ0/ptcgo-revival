from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import is_fire_energy
from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.content.definitions import Activations

def firestarter_condition(board, player_id, pokemon):
    if pokemon is None or pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_fire_energy(card) for card in discard.children)


async def fire_stream(ctx):
    await ctx.deal_damage()
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=is_fire_energy,
        prompt="Discard a Fire Energy card attached to Blaziken")
    if not discarded:
        return
    await spread_damage(10, side="opponent")(ctx)

card = PokemonCardDef(
    guid="b8167393-387b-57a6-bd8f-85dd1d575973",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Ability(
            title="Firestarter",
            game_text="Once during your turn (before your attack), you may attach a Fire Energy card from your discard pile to 1 of your Benched Pok\u00e9mon. This power can't be used if Blaziken is affected by a Special Condition.",
            effect=attach_from_discard(is_fire_energy, count=1, target=lambda p: not is_in_active_spot(p)),
            activation=Activations.ONCE_PER_TURN,
            condition=firestarter_condition,
        ),
        Attack(
            title="Fire Stream",
            game_text="Discard a Fire Energy card attached to Blaziken. If you do, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=fire_stream,
        ),
    ],
)