from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import evolve_from_deck_attack, flip_or_nothing

card = PokemonCardDef(
    guid="4c4d98f5-8a0c-570d-bb56-ae453fae85f5",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    display_name="Caterpie",
    searchable_by=["Caterpie", "Basic", "Caterpie"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=10,
    abilities=[
        Ability(
            title="Pupate",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=flip_or_nothing(then=evolve_from_deck_attack()),
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)