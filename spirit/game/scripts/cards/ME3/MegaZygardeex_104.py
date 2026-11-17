from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9e987c70-746b-53a9-8ae0-b73d4ca612a0",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaZygardeex.Name",
    display_name="Mega Zygarde ex",
    searchable_by=["Mega Zygarde ex", "Basic", "MEGA", "ex", "MegaZygardeex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=104,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Gaia Wave",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3},
            damage=200,
            effect=unimplemented,
        ),
        Attack(
            title="Nullifying Zero",
            game_text="For each of your opponent's Pok\u00e9mon, flip a coin. If heads, this attack does 150 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 5},
            effect=unimplemented,
        ),
    ],
)