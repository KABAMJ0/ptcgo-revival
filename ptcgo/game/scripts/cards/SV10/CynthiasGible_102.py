from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="33847945-293d-5145-936f-56e7c235b252",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGible.Name",
    display_name="Cynthia's Gible",
    searchable_by=["Cynthia's Gible", "Basic", "CynthiasGible"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SV10",
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
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
    ],
)