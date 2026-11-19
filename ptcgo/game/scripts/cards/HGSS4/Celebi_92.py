from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import is_in_active_spot, shield_source_next_turn, unafflicted
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_grass(card) -> bool:
    return energy_provides_type(card, PokemonTypes.GRASS.value)


def _forest_breath_ready(board, player_id, pokemon) -> bool:
    return is_in_active_spot(pokemon) and unafflicted(board, player_id, pokemon)

card = PokemonCardDef(
    guid="64d0a165-d7ce-543b-86b7-62c11876fa94",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Prime", "Celebi"],
    subtypes=["Basic", "Prime"],
    collector_number=92,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Forest Breath",
            game_text="Once during your turn (before your attack), if Celebi is your Active Pok\u00e9mon, you may attach a Grass Energy card from your hand to 1 of your Pok\u00e9mon. This power can't be used if Celebi is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_forest_breath_ready,
            effect=attach_from_hand(_is_grass, count=1, target="choice"),
        ),
        Attack(
            title="Time Circle",
            game_text="During your opponent's next turn, prevent all damage done to Celebi by attacks from your opponent's Stage 1 or Stage 2 Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)
