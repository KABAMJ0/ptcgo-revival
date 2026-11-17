from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="81613fe3-f926-5c6a-b464-eae79714dbf7",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaFeraligatrex.Name",
    display_name="Mega Feraligatr ex",
    searchable_by=["Mega Feraligatr ex", "Stage 2", "MEGA", "ex", "MegaFeraligatrex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=43,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=370,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Mortal Crunch",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 200 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)