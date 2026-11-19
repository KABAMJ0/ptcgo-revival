from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="176a9ad7-f2d2-5efa-a0dd-908db043d265",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name",
    display_name="Keldeo",
    searchable_by=["Keldeo", "Basic", "Keldeo"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=647,
    abilities=[
        Attack(
            title="Bail Out",
            game_text="Put a Water Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Resolute Blade",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), 20, base=20),
        ),
    ],
)