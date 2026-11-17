from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="69d0934b-d744-5f1a-a06a-0d222890edef",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Budew.Name",
    display_name="Budew",
    searchable_by=["Budew", "Basic", "Budew"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=406,
    abilities=[
        Attack(
            title="Itchy Pollen",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={},
            damage=10,
            effect=unimplemented,
        ),
    ],
)