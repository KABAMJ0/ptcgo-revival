from ptcgo.game.data_utils import (PokemonCardDef, Attack, Ability,
                                      Triggers, unimplemented)
from ptcgo.game.attributes import (PokemonTypes, PokemonStage, Rarities,
                                   SpecialConditions)
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.support_common import switch_self_attack



card = PokemonCardDef(
    guid="4bd62747-2043-502e-a5b7-8e081e3046c6",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GliscorLVX.Name",
    display_name="Gliscor LV.X",
    searchable_by=["Gliscor LV.X", "Level-Up", "GliscorLVX"],
    subtypes=["Level-Up"],
    collector_number=141,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    family_id=207,
    abilities=[
        Ability(
            title="Shoot Poison",
            game_text="Once during your turn (before your attack), when you put Gliscor LV.X from your hand onto your Active Gliscor, you may choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Paralyzed and Poisoned.",
            trigger=Triggers.ON_EVOLVE,
            effect=condition_attack(SpecialConditions.PARALYZED,
                                    SpecialConditions.POISONED, damage=0),
        ),
        Attack(
            title="Night Slash",
            game_text="You may switch Gliscor with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=switch_self_attack(optional=True),
        ),
    ],
)