from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonToolCardDef(
    guid="9a0c4d11-95e0-557a-9419-44218056fec8",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GScope.Name",
    display_name="G Scope",
    searchable_by=["G Scope", "Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    collector_number=93,
    set_code="BW10",
    rarity=Rarities.Rare,
    granted_abilities=[
        Attack(
            title="G Scope",
            game_text="This attack does 100 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness or Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(100, pool="bench"),
        ),
    ],
)
