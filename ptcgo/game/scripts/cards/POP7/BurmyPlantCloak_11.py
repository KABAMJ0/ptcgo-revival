from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.attributes import PokemonTypes
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.support_common import attach_from_discard


def _basic_grass_energy(card):
    return (is_basic_energy_card(card)
            and energy_provides_type(card, PokemonTypes.GRASS.value))


def _wear_cloak_condition(board, player_id, pokemon):
    return pokemon is not None and is_in_active_spot(pokemon)


from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c34ebe46-8fce-5567-8fdc-dcf9928a2d08",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyPlantCloak.Name",
    display_name="Burmy Plant Cloak",
    searchable_by=["Burmy Plant Cloak", "Basic", "BurmyPlantCloak"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="POP7",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=412,
    abilities=[
        Ability(
            title="Wear Cloak",
            game_text="Once during your turn (before your attack), if Burmy Plant Cloak is your Active Pok\u00e9mon, you may search your discard pile for a basic Grass Energy card and attach it to Burmy Plant Cloak.",
            activation=Activations.ONCE_PER_TURN,
            condition=_wear_cloak_condition,
            effect=attach_from_discard(_basic_grass_energy, count=1,
                                       target="self"),
        ),
        Attack(
            title="Plant Cloak Tackle",
            game_text="If Burmy Plant Cloak has any Grass Energy attached to it, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)