from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack, spread_damage

card = PokemonCardDef(
    guid="026f26af-1a84-579f-a5ff-c5bd1a6eed46",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Zygarde"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Rumble",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Geostrike",
            game_text="This attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=spread_damage(10, side="mine", also_base=True),
        ),
    ],
)