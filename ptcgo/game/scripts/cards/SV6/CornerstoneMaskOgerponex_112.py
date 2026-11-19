from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="b465ddeb-c09e-54c5-9f00-2bdc77c97cee",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CornerstoneMaskOgerponex.Name",
    display_name="Cornerstone Mask Ogerpon ex",
    searchable_by=["Cornerstone Mask Ogerpon ex", "Basic", "Tera", "ex", "CornerstoneMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=112,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Ability(
            title="Cornerstone Stance",
            game_text="Prevent all damage from attacks done to this Pok\u00e9mon by your opponent's Pok\u00e9mon that have an Ability.",
            effect=unimplemented,
        ),
        Attack(
            title="Demolish",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True, ignore_target_effects=True),
        ),
    ],
)