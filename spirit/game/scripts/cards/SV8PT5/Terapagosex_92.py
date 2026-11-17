from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1cae1104-49e6-58ae-854a-2ddc958e0d29",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terapagosex.Name",
    display_name="Terapagos ex",
    searchable_by=["Terapagos ex", "Basic", "ex", "Terapagosex"],
    subtypes=["Basic", "ex"],
    collector_number=92,
    set_code="SV8PT5",
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