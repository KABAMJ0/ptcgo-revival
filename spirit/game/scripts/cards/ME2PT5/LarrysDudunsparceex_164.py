from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01a59f28-db3e-56e9-b8cc-c7b84ee4ea15",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysDudunsparceex.Name",
    display_name="Larry's Dudunsparce ex",
    searchable_by=["Larry's Dudunsparce ex", "Stage 1", "ex", "LarrysDudunsparceex"],
    subtypes=["Stage 1", "ex"],
    collector_number=164,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysDunsparce.Name",
    family_id=206,
    abilities=[
        Attack(
            title="Work Rush",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)