from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="14b5bc3e-131f-511f-95a3-89bf2e49877f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchompex.Name",
    display_name="Garchomp ex",
    searchable_by=["Garchomp ex", "Stage 2", "Tera", "ex", "Garchompex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=260,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Hydro Lander",
            game_text="Attach up to 3 Basic Fighting Energy cards from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=160,
            effect=unimplemented,
        ),
        Attack(
            title="Sonic Dive",
            game_text="Discard 2 Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)