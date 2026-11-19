from ptcgo.game.card_effects.attacks_common import bonus_if, defender_is_evolved
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="11f0b89a-1a36-56bf-b13e-d0e0b89868f1",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rampardos.Name",
    display_name="Rampardos",
    searchable_by=["Rampardos", "Stage 2", "Rampardos"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    family_id=408,
    abilities=[
        Attack(
            title="Clean Hit",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(defender_is_evolved, 60),
        ),
        Attack(
            title="Wild Crash",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, it is Knocked Out.",
            cost={PokemonTypes.FIGHTING: 3},
            effect=unimplemented,
        ),
    ],
)