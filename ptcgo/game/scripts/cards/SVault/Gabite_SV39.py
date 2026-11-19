from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import evolve_from_deck_attack

card = PokemonCardDef(
    guid="cd6bfaf7-2a4a-58ce-9b4b-db09bc30a609",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    display_name="Gabite",
    searchable_by=["Gabite", "Stage 1", "Gabite"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Ascension",
            game_text="Search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=evolve_from_deck_attack(),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)