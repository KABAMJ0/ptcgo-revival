from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="89eea6b9-9fa7-568c-b1f7-bf59ebab12a9",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair", "Stage 1", "Dragonair"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Search and Invite",
            game_text="Search your deck for up to 2 Pok\u00e9mon, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)