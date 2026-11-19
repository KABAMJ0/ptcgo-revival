from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per

card = PokemonCardDef(
    guid="616b4e6b-273f-517e-949b-f23995bedbb2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=311,
    abilities=[
        Attack(
            title="Plus Damage",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), per=10, base=10),
        ),
    ],
)