from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1cfb8ea9-25dd-5bd5-99bb-c8759d881394",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terapagosex.Name",
    display_name="Terapagos ex",
    searchable_by=["Terapagos ex", "Basic", "Tera", "ex", "Terapagosex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=179,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1024,
    abilities=[
        Attack(
            title="Unified Beatdown",
            game_text="If you go second, you can't use this attack during your first turn. This attack does 30 damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Crown Opal",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic non-Colorless Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)