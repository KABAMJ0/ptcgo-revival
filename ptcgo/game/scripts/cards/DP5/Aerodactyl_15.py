from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="79d1e7d5-5b43-5a62-a3ec-3c82afbdd763",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl", "Stage 1", "Aerodactyl"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OldAmber.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Primal Claw",
            game_text="After your opponent's Pok\u00e9mon uses a Pok\u00e9-Power, put 2 damage counters on that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)