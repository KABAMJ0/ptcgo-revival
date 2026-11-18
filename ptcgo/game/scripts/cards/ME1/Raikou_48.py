from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="88fc9437-ce6e-55f9-8f86-e7769ab1f415",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Electro Fall",
            game_text="If you have at least 4 Lightning Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)