from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

from ptcgo.game.card_effects.attacks_common import bonus_if, has_damage


card = PokemonCardDef(
    guid="2cfd27cf-a2c9-532a-9f0e-83ee13b5b792",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Ursaring"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Attack(
            title="Bear Hug",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Rend",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 40 damage plus 20 more damage. If not, this attack does 40 damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            damage_operator="+",
            effect=bonus_if(has_damage("defender"), 20, base=40),
        ),
    ],
)