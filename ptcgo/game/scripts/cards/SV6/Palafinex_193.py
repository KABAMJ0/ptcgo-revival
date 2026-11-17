from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b7072cfb-3729-5fce-bee8-7d2edbf2e5e9",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafinex.Name",
    display_name="Palafin ex",
    searchable_by=["Palafin ex", "Stage 1", "ex", "Palafinex"],
    subtypes=["Stage 1", "ex"],
    collector_number=193,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    abilities=[
        Ability(
            title="Hero's Spirit",
            game_text="Put this Pok\u00e9mon into play only with the effect of Palafin's Zero to Hero Ability.",
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 1},
            damage=250,
            effect=unimplemented,
        ),
    ],
)