from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="280749e3-2aac-53bf-a1e4-6c04c7a6f0a8",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteonex.Name",
    display_name="Jolteon ex",
    searchable_by=["Jolteon ex", "Stage 1", "Tera", "ex", "Jolteonex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=153,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Flashing Spear",
            game_text="You may discard up to 2 Basic Energy from your Benched Pok\u00e9mon. This attack does 90 more damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Dravite",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=280,
            effect=unimplemented,
        ),
    ],
)