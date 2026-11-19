from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="014dd46d-0690-5845-a1db-914230f7673f",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiGX.Name",
    display_name="Darkrai-GX",
    searchable_by=["Darkrai-GX", "Basic", "GX", "DarkraiGX"],
    subtypes=["Basic", "GX"],
    collector_number=70,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=491,
    abilities=[
        Ability(
            title="Restoration",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. Then, attach a Darkness Energy card from your discard pile to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Dark Cleave",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
        Attack(
            title="Dead End-GX",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, that Pok\u00e9mon is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)