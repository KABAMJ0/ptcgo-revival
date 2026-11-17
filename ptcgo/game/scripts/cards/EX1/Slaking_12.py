from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="05ba3cf9-5324-5441-be6f-1d585275a3db",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Lazy",
            game_text="As long as Slaking is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon can't use any Pok\u00e9-Powers.",
            effect=unimplemented,
        ),
        Attack(
            title="Critical Move",
            game_text="Discard a basic Energy card attached to Slaking or this attack does nothing. Slaking can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)