from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e871fd1c-6813-5b9e-9769-abce78383803",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaScraftyex.Name",
    display_name="Mega Scrafty ex",
    searchable_by=["Mega Scrafty ex", "Stage 1", "MEGA", "ex", "MegaScraftyex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=135,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Ability(
            title="Counterattacking Crest",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), place 5 damage counters on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Outlaw Leg",
            game_text="Discard a random card from your opponent's hand. Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)