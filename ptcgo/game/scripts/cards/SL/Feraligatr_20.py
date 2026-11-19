from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="0cfc80c4-fa7c-55e2-99da-8ff3d7247d26",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SL",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=discard_opponent_energy_attack(1),
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)