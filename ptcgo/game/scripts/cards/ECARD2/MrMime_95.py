from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d1af4165-d5de-5294-90ed-9c13c60f410c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Ability(
            title="Energy Barrier",
            game_text="If Mr. Mime would be damaged by an attack, reduce that damage by 10 for each basic Energy card attached to Mr. Mime. The maximum amount of damage that can be reduced by Energy Barrier is 20.",
            effect=unimplemented,
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness and Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)