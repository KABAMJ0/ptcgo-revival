from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2fbc30d8-2410-529c-9d7c-62536b198191",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BloodmoonUrsaluna.Name",
    display_name="Bloodmoon Ursaluna",
    searchable_by=["Bloodmoon Ursaluna", "Basic", "BloodmoonUrsaluna"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=901,
    abilities=[
        Ability(
            title="Battle-Hardened",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach up to 2 Basic Fighting Energy cards from your hand to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Mad Bite",
            game_text="This attack does 30 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 30, base=100),
        ),
    ],
)