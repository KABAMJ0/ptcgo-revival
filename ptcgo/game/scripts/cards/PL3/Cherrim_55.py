from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7b0765be-41ee-5e86-94bd-0bd55ed55236",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name",
    display_name="Cherrim",
    searchable_by=["Cherrim", "Stage 1", "Cherrim"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    family_id=420,
    abilities=[
        Attack(
            title="Ram",
            cost={},
            damage=20,
        ),
        Attack(
            title="Petal Dance",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads. Cherrim is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)