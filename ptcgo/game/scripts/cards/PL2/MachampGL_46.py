from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_evolution_pokemon
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="c299e9cc-16a6-5f6f-aa04-2cbfa816b335",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampGL.Name",
    display_name="Machamp GL",
    searchable_by=["Machamp GL", "Basic", "SP", "MachampGL"],
    subtypes=["Basic", "SP"],
    collector_number=46,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=68,
    abilities=[
        Attack(
            title="Cross-Cut",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_evolution_pokemon(ctx.defender), 20),
        ),
        Attack(
            title="Brush Off",
            game_text="Put the Defending Pok\u00e9mon and all cards attached to it on top of your opponent's deck. Your opponent shuffles his or her deck afterward. (If your opponent doesn't have any Benched Pok\u00e9mon, this attack does nothing.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)