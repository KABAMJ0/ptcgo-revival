from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="dfd0ae6e-8e7f-5366-9695-00d5dac401e7",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name",
    display_name="Shiinotic",
    searchable_by=["Shiinotic", "Stage 1", "Shiinotic"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    family_id=755,
    abilities=[
        Ability(
            title="Illuminate",
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(
                lambda card: is_pokemon_of_type(card, "grass"),
                count=1,
                reveal=True,
            ),
        ),
        Attack(
            title="Flickering Spores",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)