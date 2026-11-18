from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a59454c-762f-59e7-92e9-875e47900ca2",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Excited Heal",
            game_text="Once during your turn, if you have any Grass Mega Evolution Pok\u00e9mon ex in play, you may use this Ability. Heal 60 damage from 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)