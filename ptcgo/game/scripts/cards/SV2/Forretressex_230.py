from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.content.definitions import Activations
from ptcgo.game.session.passives import is_basic_energy

def _basic_grass_energy(card):
    return is_basic_energy(card) and energy_provides_type(
        card, PokemonTypes.GRASS.value)


exploding_energy = search_attach_energy(_basic_grass_energy, count=5,
                                        distribute=True,
                                        prompt="Choose up to 5 Basic Grass Energy cards to attach")


def _exploding_energy_offered(board, player_id, pokemon):
    area = board.find_player_area(player_id, "deck")
    return any(_basic_grass_energy(card)
               for card in (area.children if area else []))


card = PokemonCardDef(
    guid="a7964117-b804-5af0-b207-b9e2e0e45725",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretressex.Name",
    display_name="Forretress ex",
    searchable_by=["Forretress ex", "Stage 1", "Tera", "ex", "Forretressex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=230,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Ability(
            title="Exploding Energy",
            game_text="Once during your turn, you may search your deck for up to 5 Basic Grass Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck. If you searched your deck in this way, this Pok\u00e9mon is Knocked Out.",
            effect=exploding_energy,
            activation=Activations.ONCE_PER_TURN,
            condition=_exploding_energy_offered,
        ),
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2},
            damage=120,
            effect=protect_next_turn(reduce=30),
        ),
    ],
)