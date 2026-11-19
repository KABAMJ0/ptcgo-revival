from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import place_counters

card = PokemonCardDef(
    guid="42875cb6-5f32-56dc-87bb-372f7988be5f",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Fainting Spell",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an opponent's attack, flip a coin. If heads, the Attacking Pok\u00e9mon is Knocked Out.",
            effect=unimplemented,
        ),
        Attack(
            title="Cursed Drop",
            game_text="Put 6 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=place_counters(6, target="choose_any_opponent"),
        ),
    ],
)