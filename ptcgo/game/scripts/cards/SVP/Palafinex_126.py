from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f228b890-0bae-5b87-b440-ab45a0f6ea5e",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafinex.Name",
    display_name="Palafin ex",
    searchable_by=["Palafin ex", "Stage 1", "ex", "Palafinex"],
    subtypes=["Stage 1", "ex"],
    collector_number=126,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=340,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=964,
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