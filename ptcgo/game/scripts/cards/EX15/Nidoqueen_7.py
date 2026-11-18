from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.session.effects import is_evolution_pokemon
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.trainers import any_of

card = PokemonCardDef(
    guid="a8c65854-b5e8-599e-a04b-0f67f288ae19",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen δ",
    searchable_by=["Nidoqueen \u03b4", "Stage 2", "Nidoqueen"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=31,
    abilities=[
        Ability(
            title="Invitation",
            game_text="Once during your turn (before your attack), you may search your deck for a Basic Pok\u00e9mon or Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Nidoqueen is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: not pokemon.get_attribute(
                AttrID.SPECIAL_CONDITIONS),
            effect=search_to_hand(
                any_of(is_basic_pokemon, is_evolution_pokemon),
                count=1,
                reveal=True,
            ),
        ),
        Attack(
            title="Vengeance",
            game_text="Does 30 damage plus 10 more damage for each Basic Pok\u00e9mon and each Evolution card in your discard pile. You can't add more than 60 damage in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)