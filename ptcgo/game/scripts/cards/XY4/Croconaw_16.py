from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="fbf73f62-ca53-5003-9afb-c8481509bbcd",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    display_name="Croconaw",
    searchable_by=["Croconaw", "Stage 1", "Croconaw"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=flip_discard_opponent_energy(),
        ),
    ],
)