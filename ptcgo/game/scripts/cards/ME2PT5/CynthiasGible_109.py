from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="c0a70548-9e0d-5f6c-9f0c-1338c34f8a0d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGible.Name",
    display_name="Cynthia's Gible",
    searchable_by=["Cynthia's Gible", "Basic", "CynthiasGible"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=443,
    abilities=[
        Attack(
            title="Rock Hurl",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
    ],
)