from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, has_damage


card = PokemonCardDef(
    guid="baaf563a-a123-5355-904a-408348ea30be",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name",
    display_name="Lycanroc",
    searchable_by=["Lycanroc", "Stage 1", "Lycanroc"],
    subtypes=["Stage 1"],
    collector_number=117,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Attack(
            title="Finishing Fang",
            game_text="If your opponent's Active Pok\u00e9mon has no damage counters on it before this attack does damage, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=90,
            effect=bonus_if(has_damage('defender'), 0, else_nothing=True),
        ),
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)