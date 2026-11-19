from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import is_water_energy
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

def water_call_condition(board, player_id, pokemon):
    if pokemon is None or pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_water_energy(card) for card in hand.children)


async def water_call(ctx):
    await attach_from_hand(
        is_water_energy, count=1, target="choice",
        target_pred=is_in_active_spot, minimum=0,
        prompt="Attach a Water Energy card from your hand to your Active Pokemon",
    )(ctx)

card = PokemonCardDef(
    guid="da920ce6-4f2f-531b-ab6e-ca41e2f462ad",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name",
    display_name="Swampert",
    searchable_by=["Swampert", "Stage 2", "Swampert"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Water Call",
            game_text="Once during your turn (before your attack), you may attach a Water Energy card from your hand to your Active Pok\u00e9mon. This power can't be used if Swampert is affected by a Special Condition.",
            effect=water_call,
            activation=Activations.ONCE_PER_TURN,
            condition=water_call_condition,
        ),
        Attack(
            title="Hypno Splash",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)