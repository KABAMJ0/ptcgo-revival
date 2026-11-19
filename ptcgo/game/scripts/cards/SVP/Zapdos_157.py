from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="ab61dd73-42a6-5565-a199-5c4990577cfb",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=157,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Follow-Up Bolt",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 10, base=20),
        ),
        Attack(
            title="Drill Peck",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)