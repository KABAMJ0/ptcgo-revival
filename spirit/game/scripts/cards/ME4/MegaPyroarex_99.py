from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="61f7fc1b-e33f-5924-b0a9-e532f3c9fc6f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaPyroarex.Name",
    display_name="Mega Pyroar ex",
    searchable_by=["Mega Pyroar ex", "Stage 1", "MEGA", "ex", "MegaPyroarex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=99,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Attack(
            title="Ferocious Bellow",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon do 50 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Fiery Big Bang",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=290,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)