from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dfce3c61-6ecf-5bd7-94f4-98089acde512",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Ursaring"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="HGSS2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Attack(
            title="Confront",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Cross Chop",
            game_text="Flip a coin. If heads, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)