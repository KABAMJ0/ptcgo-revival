from ptcgo.game.card_effects.passives_common import flip_prevent_damage_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cf282789-0b68-503d-aaf9-08259aac4f21",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccinoex.Name",
    display_name="Cinccino ex",
    searchable_by=["Cinccino ex", "Stage 1", "ex", "Cinccinoex"],
    subtypes=["Stage 1", "ex"],
    collector_number=73,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=240,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Ability(
            title="Smooth Coat",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, prevent that damage.",
            passive=flip_prevent_damage_passive("Smooth Coat"),
        ),
        Attack(
            title="Energized Slap",
            game_text="This attack does 40 damage for each Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
