from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_defender_tools_then_damage

card = PokemonCardDef(
    guid="30e9c2e8-feb6-591b-a798-254a45e1e3dd",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Raticate"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Scrape Off",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=discard_defender_tools_then_damage(),
        ),
        Attack(
            title="Retaliatory Incisors",
            game_text="This attack does 40 damage for each damage counter on all of your Benched Rattata.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)