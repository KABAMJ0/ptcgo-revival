from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="457c1866-6b71-5fdc-a1f9-2ff41e2175c1",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic", "Drampa"],
    subtypes=["Basic"],
    collector_number=161,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=780,
    abilities=[
        Attack(
            title="Outrage",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), per=10, base=60),
        ),
    ],
)