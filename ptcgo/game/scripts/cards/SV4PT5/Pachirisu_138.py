from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="3edbf10e-44ab-52b7-86aa-0a840e0d9fe2",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=417,
    abilities=[
        Ability(
            title="Electricity Pouches",
            game_text="This Pok\u00e9mon can't be Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Everyone Discharge",
            game_text="This attack does 20 more damage for each of your Benched Lightning Pok\u00e9mon. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ignore_modifier_attack(ignore_weakness=True),
        ),
    ],
)