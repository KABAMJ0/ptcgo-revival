from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3db597ad-2bef-5e66-ad50-31c4871c64dd",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAggron.Name",
    display_name="Team Magma's Aggron",
    searchable_by=["Team Magma's Aggron", "Stage 2", "TeamMagmasAggron"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasLairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Crush",
            game_text="Flip a coin for each Energy attached to Team Magma's Aggron. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Land Stream",
            game_text="You may discard any number of basic Energy cards attached to Team Magma's Aggron. If you do, this attack does 50 damage plus 20 more damage for each basic Energy card you discarded.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)