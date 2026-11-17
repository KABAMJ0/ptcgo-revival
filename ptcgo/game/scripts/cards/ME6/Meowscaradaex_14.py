from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c35587a-43b9-5eab-b72f-17415fe1a289",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowscaradaex.Name",
    display_name="Meowscarada ex",
    searchable_by=["Meowscarada ex", "Stage 2", "ex", "Meowscaradaex"],
    subtypes=["Stage 2", "ex"],
    collector_number=14,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    family_id=906,
    abilities=[
        Attack(
            title="Magical Bullet",
            game_text="This attack also does 120 damage to 1 of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)